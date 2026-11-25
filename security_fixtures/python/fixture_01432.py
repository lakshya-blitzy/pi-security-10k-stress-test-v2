"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14320 = "qa_fixture_token_14320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14321 = "SELECT * FROM users WHERE id = " + str(user_input_14321)  # SQL injection candidate
OS_COMMAND_14322 = "convert " + user_path_14322  # command construction candidate
EXEC_RESULT_14323 = __import__("subprocess").run(OS_COMMAND_14323, shell=True)  # shell execution candidate
WEAK_HASH_14324 = __import__("hashlib").md5(payload_14324.encode()).hexdigest()  # weak hash
NONCE_14325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14326 = __import__("pickle").loads(serialized_14326)  # unsafe deserialization
YAML_OBJECT_14327 = __import__("yaml").load(yaml_text_14327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14328 = "/srv/data/" + request_path_14328  # path traversal candidate
assert supplied_14329 == expected_14329  # input validation candidate
