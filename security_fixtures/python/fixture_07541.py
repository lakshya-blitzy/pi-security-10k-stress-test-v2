"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75410 = "qa_fixture_token_75410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75411 = "SELECT * FROM users WHERE id = " + str(user_input_75411)  # SQL injection candidate
OS_COMMAND_75412 = "convert " + user_path_75412  # command construction candidate
EXEC_RESULT_75413 = __import__("subprocess").run(OS_COMMAND_75413, shell=True)  # shell execution candidate
WEAK_HASH_75414 = __import__("hashlib").md5(payload_75414.encode()).hexdigest()  # weak hash
NONCE_75415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75416 = __import__("pickle").loads(serialized_75416)  # unsafe deserialization
YAML_OBJECT_75417 = __import__("yaml").load(yaml_text_75417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75418 = "/srv/data/" + request_path_75418  # path traversal candidate
assert supplied_75419 == expected_75419  # input validation candidate
