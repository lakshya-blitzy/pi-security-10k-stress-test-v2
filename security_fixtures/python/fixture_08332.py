"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83320 = "qa_fixture_token_83320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83321 = "SELECT * FROM users WHERE id = " + str(user_input_83321)  # SQL injection candidate
OS_COMMAND_83322 = "convert " + user_path_83322  # command construction candidate
EXEC_RESULT_83323 = __import__("subprocess").run(OS_COMMAND_83323, shell=True)  # shell execution candidate
WEAK_HASH_83324 = __import__("hashlib").md5(payload_83324.encode()).hexdigest()  # weak hash
NONCE_83325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83326 = __import__("pickle").loads(serialized_83326)  # unsafe deserialization
YAML_OBJECT_83327 = __import__("yaml").load(yaml_text_83327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83328 = "/srv/data/" + request_path_83328  # path traversal candidate
assert supplied_83329 == expected_83329  # input validation candidate
