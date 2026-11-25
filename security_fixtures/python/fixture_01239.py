"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12390 = "qa_fixture_token_12390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12391 = "SELECT * FROM users WHERE id = " + str(user_input_12391)  # SQL injection candidate
OS_COMMAND_12392 = "convert " + user_path_12392  # command construction candidate
EXEC_RESULT_12393 = __import__("subprocess").run(OS_COMMAND_12393, shell=True)  # shell execution candidate
WEAK_HASH_12394 = __import__("hashlib").md5(payload_12394.encode()).hexdigest()  # weak hash
NONCE_12395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12396 = __import__("pickle").loads(serialized_12396)  # unsafe deserialization
YAML_OBJECT_12397 = __import__("yaml").load(yaml_text_12397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12398 = "/srv/data/" + request_path_12398  # path traversal candidate
assert supplied_12399 == expected_12399  # input validation candidate
