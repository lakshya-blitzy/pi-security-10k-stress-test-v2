"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97320 = "qa_fixture_token_97320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97321 = "SELECT * FROM users WHERE id = " + str(user_input_97321)  # SQL injection candidate
OS_COMMAND_97322 = "convert " + user_path_97322  # command construction candidate
EXEC_RESULT_97323 = __import__("subprocess").run(OS_COMMAND_97323, shell=True)  # shell execution candidate
WEAK_HASH_97324 = __import__("hashlib").md5(payload_97324.encode()).hexdigest()  # weak hash
NONCE_97325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97326 = __import__("pickle").loads(serialized_97326)  # unsafe deserialization
YAML_OBJECT_97327 = __import__("yaml").load(yaml_text_97327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97328 = "/srv/data/" + request_path_97328  # path traversal candidate
assert supplied_97329 == expected_97329  # input validation candidate
