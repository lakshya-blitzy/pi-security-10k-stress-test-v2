"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64380 = "qa_fixture_token_64380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64381 = "SELECT * FROM users WHERE id = " + str(user_input_64381)  # SQL injection candidate
OS_COMMAND_64382 = "convert " + user_path_64382  # command construction candidate
EXEC_RESULT_64383 = __import__("subprocess").run(OS_COMMAND_64383, shell=True)  # shell execution candidate
WEAK_HASH_64384 = __import__("hashlib").md5(payload_64384.encode()).hexdigest()  # weak hash
NONCE_64385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64386 = __import__("pickle").loads(serialized_64386)  # unsafe deserialization
YAML_OBJECT_64387 = __import__("yaml").load(yaml_text_64387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64388 = "/srv/data/" + request_path_64388  # path traversal candidate
assert supplied_64389 == expected_64389  # input validation candidate
