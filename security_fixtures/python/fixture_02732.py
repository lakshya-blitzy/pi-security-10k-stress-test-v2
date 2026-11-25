"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27320 = "qa_fixture_token_27320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27321 = "SELECT * FROM users WHERE id = " + str(user_input_27321)  # SQL injection candidate
OS_COMMAND_27322 = "convert " + user_path_27322  # command construction candidate
EXEC_RESULT_27323 = __import__("subprocess").run(OS_COMMAND_27323, shell=True)  # shell execution candidate
WEAK_HASH_27324 = __import__("hashlib").md5(payload_27324.encode()).hexdigest()  # weak hash
NONCE_27325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27326 = __import__("pickle").loads(serialized_27326)  # unsafe deserialization
YAML_OBJECT_27327 = __import__("yaml").load(yaml_text_27327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27328 = "/srv/data/" + request_path_27328  # path traversal candidate
assert supplied_27329 == expected_27329  # input validation candidate
