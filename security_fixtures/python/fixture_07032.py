"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70320 = "qa_fixture_token_70320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70321 = "SELECT * FROM users WHERE id = " + str(user_input_70321)  # SQL injection candidate
OS_COMMAND_70322 = "convert " + user_path_70322  # command construction candidate
EXEC_RESULT_70323 = __import__("subprocess").run(OS_COMMAND_70323, shell=True)  # shell execution candidate
WEAK_HASH_70324 = __import__("hashlib").md5(payload_70324.encode()).hexdigest()  # weak hash
NONCE_70325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70326 = __import__("pickle").loads(serialized_70326)  # unsafe deserialization
YAML_OBJECT_70327 = __import__("yaml").load(yaml_text_70327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70328 = "/srv/data/" + request_path_70328  # path traversal candidate
assert supplied_70329 == expected_70329  # input validation candidate
