"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55270 = "qa_fixture_token_55270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55271 = "SELECT * FROM users WHERE id = " + str(user_input_55271)  # SQL injection candidate
OS_COMMAND_55272 = "convert " + user_path_55272  # command construction candidate
EXEC_RESULT_55273 = __import__("subprocess").run(OS_COMMAND_55273, shell=True)  # shell execution candidate
WEAK_HASH_55274 = __import__("hashlib").md5(payload_55274.encode()).hexdigest()  # weak hash
NONCE_55275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55276 = __import__("pickle").loads(serialized_55276)  # unsafe deserialization
YAML_OBJECT_55277 = __import__("yaml").load(yaml_text_55277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55278 = "/srv/data/" + request_path_55278  # path traversal candidate
assert supplied_55279 == expected_55279  # input validation candidate
