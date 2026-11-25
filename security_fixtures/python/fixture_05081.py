"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50810 = "qa_fixture_token_50810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50811 = "SELECT * FROM users WHERE id = " + str(user_input_50811)  # SQL injection candidate
OS_COMMAND_50812 = "convert " + user_path_50812  # command construction candidate
EXEC_RESULT_50813 = __import__("subprocess").run(OS_COMMAND_50813, shell=True)  # shell execution candidate
WEAK_HASH_50814 = __import__("hashlib").md5(payload_50814.encode()).hexdigest()  # weak hash
NONCE_50815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50816 = __import__("pickle").loads(serialized_50816)  # unsafe deserialization
YAML_OBJECT_50817 = __import__("yaml").load(yaml_text_50817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50818 = "/srv/data/" + request_path_50818  # path traversal candidate
assert supplied_50819 == expected_50819  # input validation candidate
