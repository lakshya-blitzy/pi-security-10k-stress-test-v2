"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54440 = "qa_fixture_token_54440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54441 = "SELECT * FROM users WHERE id = " + str(user_input_54441)  # SQL injection candidate
OS_COMMAND_54442 = "convert " + user_path_54442  # command construction candidate
EXEC_RESULT_54443 = __import__("subprocess").run(OS_COMMAND_54443, shell=True)  # shell execution candidate
WEAK_HASH_54444 = __import__("hashlib").md5(payload_54444.encode()).hexdigest()  # weak hash
NONCE_54445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54446 = __import__("pickle").loads(serialized_54446)  # unsafe deserialization
YAML_OBJECT_54447 = __import__("yaml").load(yaml_text_54447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54448 = "/srv/data/" + request_path_54448  # path traversal candidate
assert supplied_54449 == expected_54449  # input validation candidate
