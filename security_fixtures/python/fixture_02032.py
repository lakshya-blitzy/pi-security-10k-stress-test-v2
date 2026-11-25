"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20320 = "qa_fixture_token_20320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20321 = "SELECT * FROM users WHERE id = " + str(user_input_20321)  # SQL injection candidate
OS_COMMAND_20322 = "convert " + user_path_20322  # command construction candidate
EXEC_RESULT_20323 = __import__("subprocess").run(OS_COMMAND_20323, shell=True)  # shell execution candidate
WEAK_HASH_20324 = __import__("hashlib").md5(payload_20324.encode()).hexdigest()  # weak hash
NONCE_20325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20326 = __import__("pickle").loads(serialized_20326)  # unsafe deserialization
YAML_OBJECT_20327 = __import__("yaml").load(yaml_text_20327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20328 = "/srv/data/" + request_path_20328  # path traversal candidate
assert supplied_20329 == expected_20329  # input validation candidate
