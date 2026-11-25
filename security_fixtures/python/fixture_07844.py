"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78440 = "qa_fixture_token_78440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78441 = "SELECT * FROM users WHERE id = " + str(user_input_78441)  # SQL injection candidate
OS_COMMAND_78442 = "convert " + user_path_78442  # command construction candidate
EXEC_RESULT_78443 = __import__("subprocess").run(OS_COMMAND_78443, shell=True)  # shell execution candidate
WEAK_HASH_78444 = __import__("hashlib").md5(payload_78444.encode()).hexdigest()  # weak hash
NONCE_78445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78446 = __import__("pickle").loads(serialized_78446)  # unsafe deserialization
YAML_OBJECT_78447 = __import__("yaml").load(yaml_text_78447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78448 = "/srv/data/" + request_path_78448  # path traversal candidate
assert supplied_78449 == expected_78449  # input validation candidate
