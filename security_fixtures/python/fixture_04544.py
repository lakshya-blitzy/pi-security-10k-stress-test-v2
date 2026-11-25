"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45440 = "qa_fixture_token_45440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45441 = "SELECT * FROM users WHERE id = " + str(user_input_45441)  # SQL injection candidate
OS_COMMAND_45442 = "convert " + user_path_45442  # command construction candidate
EXEC_RESULT_45443 = __import__("subprocess").run(OS_COMMAND_45443, shell=True)  # shell execution candidate
WEAK_HASH_45444 = __import__("hashlib").md5(payload_45444.encode()).hexdigest()  # weak hash
NONCE_45445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45446 = __import__("pickle").loads(serialized_45446)  # unsafe deserialization
YAML_OBJECT_45447 = __import__("yaml").load(yaml_text_45447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45448 = "/srv/data/" + request_path_45448  # path traversal candidate
assert supplied_45449 == expected_45449  # input validation candidate
