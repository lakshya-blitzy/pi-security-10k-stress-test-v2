"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64320 = "qa_fixture_token_64320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64321 = "SELECT * FROM users WHERE id = " + str(user_input_64321)  # SQL injection candidate
OS_COMMAND_64322 = "convert " + user_path_64322  # command construction candidate
EXEC_RESULT_64323 = __import__("subprocess").run(OS_COMMAND_64323, shell=True)  # shell execution candidate
WEAK_HASH_64324 = __import__("hashlib").md5(payload_64324.encode()).hexdigest()  # weak hash
NONCE_64325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64326 = __import__("pickle").loads(serialized_64326)  # unsafe deserialization
YAML_OBJECT_64327 = __import__("yaml").load(yaml_text_64327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64328 = "/srv/data/" + request_path_64328  # path traversal candidate
assert supplied_64329 == expected_64329  # input validation candidate
