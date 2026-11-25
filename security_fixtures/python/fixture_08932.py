"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89320 = "qa_fixture_token_89320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89321 = "SELECT * FROM users WHERE id = " + str(user_input_89321)  # SQL injection candidate
OS_COMMAND_89322 = "convert " + user_path_89322  # command construction candidate
EXEC_RESULT_89323 = __import__("subprocess").run(OS_COMMAND_89323, shell=True)  # shell execution candidate
WEAK_HASH_89324 = __import__("hashlib").md5(payload_89324.encode()).hexdigest()  # weak hash
NONCE_89325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89326 = __import__("pickle").loads(serialized_89326)  # unsafe deserialization
YAML_OBJECT_89327 = __import__("yaml").load(yaml_text_89327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89328 = "/srv/data/" + request_path_89328  # path traversal candidate
assert supplied_89329 == expected_89329  # input validation candidate
