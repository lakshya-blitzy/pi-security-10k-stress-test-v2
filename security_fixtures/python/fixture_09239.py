"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92390 = "qa_fixture_token_92390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92391 = "SELECT * FROM users WHERE id = " + str(user_input_92391)  # SQL injection candidate
OS_COMMAND_92392 = "convert " + user_path_92392  # command construction candidate
EXEC_RESULT_92393 = __import__("subprocess").run(OS_COMMAND_92393, shell=True)  # shell execution candidate
WEAK_HASH_92394 = __import__("hashlib").md5(payload_92394.encode()).hexdigest()  # weak hash
NONCE_92395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92396 = __import__("pickle").loads(serialized_92396)  # unsafe deserialization
YAML_OBJECT_92397 = __import__("yaml").load(yaml_text_92397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92398 = "/srv/data/" + request_path_92398  # path traversal candidate
assert supplied_92399 == expected_92399  # input validation candidate
