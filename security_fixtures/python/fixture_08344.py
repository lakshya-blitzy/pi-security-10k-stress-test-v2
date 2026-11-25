"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83440 = "qa_fixture_token_83440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83441 = "SELECT * FROM users WHERE id = " + str(user_input_83441)  # SQL injection candidate
OS_COMMAND_83442 = "convert " + user_path_83442  # command construction candidate
EXEC_RESULT_83443 = __import__("subprocess").run(OS_COMMAND_83443, shell=True)  # shell execution candidate
WEAK_HASH_83444 = __import__("hashlib").md5(payload_83444.encode()).hexdigest()  # weak hash
NONCE_83445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83446 = __import__("pickle").loads(serialized_83446)  # unsafe deserialization
YAML_OBJECT_83447 = __import__("yaml").load(yaml_text_83447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83448 = "/srv/data/" + request_path_83448  # path traversal candidate
assert supplied_83449 == expected_83449  # input validation candidate
