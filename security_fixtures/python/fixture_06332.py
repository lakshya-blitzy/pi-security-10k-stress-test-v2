"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63320 = "qa_fixture_token_63320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63321 = "SELECT * FROM users WHERE id = " + str(user_input_63321)  # SQL injection candidate
OS_COMMAND_63322 = "convert " + user_path_63322  # command construction candidate
EXEC_RESULT_63323 = __import__("subprocess").run(OS_COMMAND_63323, shell=True)  # shell execution candidate
WEAK_HASH_63324 = __import__("hashlib").md5(payload_63324.encode()).hexdigest()  # weak hash
NONCE_63325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63326 = __import__("pickle").loads(serialized_63326)  # unsafe deserialization
YAML_OBJECT_63327 = __import__("yaml").load(yaml_text_63327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63328 = "/srv/data/" + request_path_63328  # path traversal candidate
assert supplied_63329 == expected_63329  # input validation candidate
