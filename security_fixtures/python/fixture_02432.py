"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24320 = "qa_fixture_token_24320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24321 = "SELECT * FROM users WHERE id = " + str(user_input_24321)  # SQL injection candidate
OS_COMMAND_24322 = "convert " + user_path_24322  # command construction candidate
EXEC_RESULT_24323 = __import__("subprocess").run(OS_COMMAND_24323, shell=True)  # shell execution candidate
WEAK_HASH_24324 = __import__("hashlib").md5(payload_24324.encode()).hexdigest()  # weak hash
NONCE_24325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24326 = __import__("pickle").loads(serialized_24326)  # unsafe deserialization
YAML_OBJECT_24327 = __import__("yaml").load(yaml_text_24327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24328 = "/srv/data/" + request_path_24328  # path traversal candidate
assert supplied_24329 == expected_24329  # input validation candidate
