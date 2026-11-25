"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15320 = "qa_fixture_token_15320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15321 = "SELECT * FROM users WHERE id = " + str(user_input_15321)  # SQL injection candidate
OS_COMMAND_15322 = "convert " + user_path_15322  # command construction candidate
EXEC_RESULT_15323 = __import__("subprocess").run(OS_COMMAND_15323, shell=True)  # shell execution candidate
WEAK_HASH_15324 = __import__("hashlib").md5(payload_15324.encode()).hexdigest()  # weak hash
NONCE_15325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15326 = __import__("pickle").loads(serialized_15326)  # unsafe deserialization
YAML_OBJECT_15327 = __import__("yaml").load(yaml_text_15327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15328 = "/srv/data/" + request_path_15328  # path traversal candidate
assert supplied_15329 == expected_15329  # input validation candidate
