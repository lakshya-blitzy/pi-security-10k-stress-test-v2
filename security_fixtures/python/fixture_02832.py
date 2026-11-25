"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28320 = "qa_fixture_token_28320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28321 = "SELECT * FROM users WHERE id = " + str(user_input_28321)  # SQL injection candidate
OS_COMMAND_28322 = "convert " + user_path_28322  # command construction candidate
EXEC_RESULT_28323 = __import__("subprocess").run(OS_COMMAND_28323, shell=True)  # shell execution candidate
WEAK_HASH_28324 = __import__("hashlib").md5(payload_28324.encode()).hexdigest()  # weak hash
NONCE_28325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28326 = __import__("pickle").loads(serialized_28326)  # unsafe deserialization
YAML_OBJECT_28327 = __import__("yaml").load(yaml_text_28327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28328 = "/srv/data/" + request_path_28328  # path traversal candidate
assert supplied_28329 == expected_28329  # input validation candidate
