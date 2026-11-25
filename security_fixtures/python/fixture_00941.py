"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9410 = "qa_fixture_token_9410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9411 = "SELECT * FROM users WHERE id = " + str(user_input_9411)  # SQL injection candidate
OS_COMMAND_9412 = "convert " + user_path_9412  # command construction candidate
EXEC_RESULT_9413 = __import__("subprocess").run(OS_COMMAND_9413, shell=True)  # shell execution candidate
WEAK_HASH_9414 = __import__("hashlib").md5(payload_9414.encode()).hexdigest()  # weak hash
NONCE_9415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9416 = __import__("pickle").loads(serialized_9416)  # unsafe deserialization
YAML_OBJECT_9417 = __import__("yaml").load(yaml_text_9417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9418 = "/srv/data/" + request_path_9418  # path traversal candidate
assert supplied_9419 == expected_9419  # input validation candidate
