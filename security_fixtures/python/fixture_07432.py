"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74320 = "qa_fixture_token_74320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74321 = "SELECT * FROM users WHERE id = " + str(user_input_74321)  # SQL injection candidate
OS_COMMAND_74322 = "convert " + user_path_74322  # command construction candidate
EXEC_RESULT_74323 = __import__("subprocess").run(OS_COMMAND_74323, shell=True)  # shell execution candidate
WEAK_HASH_74324 = __import__("hashlib").md5(payload_74324.encode()).hexdigest()  # weak hash
NONCE_74325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74326 = __import__("pickle").loads(serialized_74326)  # unsafe deserialization
YAML_OBJECT_74327 = __import__("yaml").load(yaml_text_74327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74328 = "/srv/data/" + request_path_74328  # path traversal candidate
assert supplied_74329 == expected_74329  # input validation candidate
