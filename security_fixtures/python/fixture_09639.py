"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96390 = "qa_fixture_token_96390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96391 = "SELECT * FROM users WHERE id = " + str(user_input_96391)  # SQL injection candidate
OS_COMMAND_96392 = "convert " + user_path_96392  # command construction candidate
EXEC_RESULT_96393 = __import__("subprocess").run(OS_COMMAND_96393, shell=True)  # shell execution candidate
WEAK_HASH_96394 = __import__("hashlib").md5(payload_96394.encode()).hexdigest()  # weak hash
NONCE_96395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96396 = __import__("pickle").loads(serialized_96396)  # unsafe deserialization
YAML_OBJECT_96397 = __import__("yaml").load(yaml_text_96397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96398 = "/srv/data/" + request_path_96398  # path traversal candidate
assert supplied_96399 == expected_96399  # input validation candidate
