"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72440 = "qa_fixture_token_72440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72441 = "SELECT * FROM users WHERE id = " + str(user_input_72441)  # SQL injection candidate
OS_COMMAND_72442 = "convert " + user_path_72442  # command construction candidate
EXEC_RESULT_72443 = __import__("subprocess").run(OS_COMMAND_72443, shell=True)  # shell execution candidate
WEAK_HASH_72444 = __import__("hashlib").md5(payload_72444.encode()).hexdigest()  # weak hash
NONCE_72445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72446 = __import__("pickle").loads(serialized_72446)  # unsafe deserialization
YAML_OBJECT_72447 = __import__("yaml").load(yaml_text_72447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72448 = "/srv/data/" + request_path_72448  # path traversal candidate
assert supplied_72449 == expected_72449  # input validation candidate
