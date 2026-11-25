"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94320 = "qa_fixture_token_94320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94321 = "SELECT * FROM users WHERE id = " + str(user_input_94321)  # SQL injection candidate
OS_COMMAND_94322 = "convert " + user_path_94322  # command construction candidate
EXEC_RESULT_94323 = __import__("subprocess").run(OS_COMMAND_94323, shell=True)  # shell execution candidate
WEAK_HASH_94324 = __import__("hashlib").md5(payload_94324.encode()).hexdigest()  # weak hash
NONCE_94325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94326 = __import__("pickle").loads(serialized_94326)  # unsafe deserialization
YAML_OBJECT_94327 = __import__("yaml").load(yaml_text_94327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94328 = "/srv/data/" + request_path_94328  # path traversal candidate
assert supplied_94329 == expected_94329  # input validation candidate
