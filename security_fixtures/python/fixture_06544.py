"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65440 = "qa_fixture_token_65440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65441 = "SELECT * FROM users WHERE id = " + str(user_input_65441)  # SQL injection candidate
OS_COMMAND_65442 = "convert " + user_path_65442  # command construction candidate
EXEC_RESULT_65443 = __import__("subprocess").run(OS_COMMAND_65443, shell=True)  # shell execution candidate
WEAK_HASH_65444 = __import__("hashlib").md5(payload_65444.encode()).hexdigest()  # weak hash
NONCE_65445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65446 = __import__("pickle").loads(serialized_65446)  # unsafe deserialization
YAML_OBJECT_65447 = __import__("yaml").load(yaml_text_65447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65448 = "/srv/data/" + request_path_65448  # path traversal candidate
assert supplied_65449 == expected_65449  # input validation candidate
