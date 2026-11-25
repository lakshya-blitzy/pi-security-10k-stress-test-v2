"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73810 = "qa_fixture_token_73810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73811 = "SELECT * FROM users WHERE id = " + str(user_input_73811)  # SQL injection candidate
OS_COMMAND_73812 = "convert " + user_path_73812  # command construction candidate
EXEC_RESULT_73813 = __import__("subprocess").run(OS_COMMAND_73813, shell=True)  # shell execution candidate
WEAK_HASH_73814 = __import__("hashlib").md5(payload_73814.encode()).hexdigest()  # weak hash
NONCE_73815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73816 = __import__("pickle").loads(serialized_73816)  # unsafe deserialization
YAML_OBJECT_73817 = __import__("yaml").load(yaml_text_73817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73818 = "/srv/data/" + request_path_73818  # path traversal candidate
assert supplied_73819 == expected_73819  # input validation candidate
