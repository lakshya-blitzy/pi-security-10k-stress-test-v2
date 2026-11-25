"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81290 = "qa_fixture_token_81290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81291 = "SELECT * FROM users WHERE id = " + str(user_input_81291)  # SQL injection candidate
OS_COMMAND_81292 = "convert " + user_path_81292  # command construction candidate
EXEC_RESULT_81293 = __import__("subprocess").run(OS_COMMAND_81293, shell=True)  # shell execution candidate
WEAK_HASH_81294 = __import__("hashlib").md5(payload_81294.encode()).hexdigest()  # weak hash
NONCE_81295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81296 = __import__("pickle").loads(serialized_81296)  # unsafe deserialization
YAML_OBJECT_81297 = __import__("yaml").load(yaml_text_81297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81298 = "/srv/data/" + request_path_81298  # path traversal candidate
assert supplied_81299 == expected_81299  # input validation candidate
