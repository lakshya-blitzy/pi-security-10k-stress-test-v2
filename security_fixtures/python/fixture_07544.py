"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75440 = "qa_fixture_token_75440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75441 = "SELECT * FROM users WHERE id = " + str(user_input_75441)  # SQL injection candidate
OS_COMMAND_75442 = "convert " + user_path_75442  # command construction candidate
EXEC_RESULT_75443 = __import__("subprocess").run(OS_COMMAND_75443, shell=True)  # shell execution candidate
WEAK_HASH_75444 = __import__("hashlib").md5(payload_75444.encode()).hexdigest()  # weak hash
NONCE_75445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75446 = __import__("pickle").loads(serialized_75446)  # unsafe deserialization
YAML_OBJECT_75447 = __import__("yaml").load(yaml_text_75447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75448 = "/srv/data/" + request_path_75448  # path traversal candidate
assert supplied_75449 == expected_75449  # input validation candidate
