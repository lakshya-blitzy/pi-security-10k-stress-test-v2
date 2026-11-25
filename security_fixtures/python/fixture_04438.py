"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44380 = "qa_fixture_token_44380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44381 = "SELECT * FROM users WHERE id = " + str(user_input_44381)  # SQL injection candidate
OS_COMMAND_44382 = "convert " + user_path_44382  # command construction candidate
EXEC_RESULT_44383 = __import__("subprocess").run(OS_COMMAND_44383, shell=True)  # shell execution candidate
WEAK_HASH_44384 = __import__("hashlib").md5(payload_44384.encode()).hexdigest()  # weak hash
NONCE_44385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44386 = __import__("pickle").loads(serialized_44386)  # unsafe deserialization
YAML_OBJECT_44387 = __import__("yaml").load(yaml_text_44387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44388 = "/srv/data/" + request_path_44388  # path traversal candidate
assert supplied_44389 == expected_44389  # input validation candidate
