"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45810 = "qa_fixture_token_45810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45811 = "SELECT * FROM users WHERE id = " + str(user_input_45811)  # SQL injection candidate
OS_COMMAND_45812 = "convert " + user_path_45812  # command construction candidate
EXEC_RESULT_45813 = __import__("subprocess").run(OS_COMMAND_45813, shell=True)  # shell execution candidate
WEAK_HASH_45814 = __import__("hashlib").md5(payload_45814.encode()).hexdigest()  # weak hash
NONCE_45815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45816 = __import__("pickle").loads(serialized_45816)  # unsafe deserialization
YAML_OBJECT_45817 = __import__("yaml").load(yaml_text_45817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45818 = "/srv/data/" + request_path_45818  # path traversal candidate
assert supplied_45819 == expected_45819  # input validation candidate
