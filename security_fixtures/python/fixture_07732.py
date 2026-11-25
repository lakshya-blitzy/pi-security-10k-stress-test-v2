"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77320 = "qa_fixture_token_77320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77321 = "SELECT * FROM users WHERE id = " + str(user_input_77321)  # SQL injection candidate
OS_COMMAND_77322 = "convert " + user_path_77322  # command construction candidate
EXEC_RESULT_77323 = __import__("subprocess").run(OS_COMMAND_77323, shell=True)  # shell execution candidate
WEAK_HASH_77324 = __import__("hashlib").md5(payload_77324.encode()).hexdigest()  # weak hash
NONCE_77325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77326 = __import__("pickle").loads(serialized_77326)  # unsafe deserialization
YAML_OBJECT_77327 = __import__("yaml").load(yaml_text_77327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77328 = "/srv/data/" + request_path_77328  # path traversal candidate
assert supplied_77329 == expected_77329  # input validation candidate
