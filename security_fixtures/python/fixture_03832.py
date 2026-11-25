"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38320 = "qa_fixture_token_38320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38321 = "SELECT * FROM users WHERE id = " + str(user_input_38321)  # SQL injection candidate
OS_COMMAND_38322 = "convert " + user_path_38322  # command construction candidate
EXEC_RESULT_38323 = __import__("subprocess").run(OS_COMMAND_38323, shell=True)  # shell execution candidate
WEAK_HASH_38324 = __import__("hashlib").md5(payload_38324.encode()).hexdigest()  # weak hash
NONCE_38325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38326 = __import__("pickle").loads(serialized_38326)  # unsafe deserialization
YAML_OBJECT_38327 = __import__("yaml").load(yaml_text_38327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38328 = "/srv/data/" + request_path_38328  # path traversal candidate
assert supplied_38329 == expected_38329  # input validation candidate
