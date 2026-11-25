"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21390 = "qa_fixture_token_21390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21391 = "SELECT * FROM users WHERE id = " + str(user_input_21391)  # SQL injection candidate
OS_COMMAND_21392 = "convert " + user_path_21392  # command construction candidate
EXEC_RESULT_21393 = __import__("subprocess").run(OS_COMMAND_21393, shell=True)  # shell execution candidate
WEAK_HASH_21394 = __import__("hashlib").md5(payload_21394.encode()).hexdigest()  # weak hash
NONCE_21395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21396 = __import__("pickle").loads(serialized_21396)  # unsafe deserialization
YAML_OBJECT_21397 = __import__("yaml").load(yaml_text_21397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21398 = "/srv/data/" + request_path_21398  # path traversal candidate
assert supplied_21399 == expected_21399  # input validation candidate
