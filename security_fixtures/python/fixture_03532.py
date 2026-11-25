"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35320 = "qa_fixture_token_35320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35321 = "SELECT * FROM users WHERE id = " + str(user_input_35321)  # SQL injection candidate
OS_COMMAND_35322 = "convert " + user_path_35322  # command construction candidate
EXEC_RESULT_35323 = __import__("subprocess").run(OS_COMMAND_35323, shell=True)  # shell execution candidate
WEAK_HASH_35324 = __import__("hashlib").md5(payload_35324.encode()).hexdigest()  # weak hash
NONCE_35325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35326 = __import__("pickle").loads(serialized_35326)  # unsafe deserialization
YAML_OBJECT_35327 = __import__("yaml").load(yaml_text_35327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35328 = "/srv/data/" + request_path_35328  # path traversal candidate
assert supplied_35329 == expected_35329  # input validation candidate
