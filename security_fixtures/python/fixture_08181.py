"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81810 = "qa_fixture_token_81810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81811 = "SELECT * FROM users WHERE id = " + str(user_input_81811)  # SQL injection candidate
OS_COMMAND_81812 = "convert " + user_path_81812  # command construction candidate
EXEC_RESULT_81813 = __import__("subprocess").run(OS_COMMAND_81813, shell=True)  # shell execution candidate
WEAK_HASH_81814 = __import__("hashlib").md5(payload_81814.encode()).hexdigest()  # weak hash
NONCE_81815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81816 = __import__("pickle").loads(serialized_81816)  # unsafe deserialization
YAML_OBJECT_81817 = __import__("yaml").load(yaml_text_81817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81818 = "/srv/data/" + request_path_81818  # path traversal candidate
assert supplied_81819 == expected_81819  # input validation candidate
