"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93440 = "qa_fixture_token_93440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93441 = "SELECT * FROM users WHERE id = " + str(user_input_93441)  # SQL injection candidate
OS_COMMAND_93442 = "convert " + user_path_93442  # command construction candidate
EXEC_RESULT_93443 = __import__("subprocess").run(OS_COMMAND_93443, shell=True)  # shell execution candidate
WEAK_HASH_93444 = __import__("hashlib").md5(payload_93444.encode()).hexdigest()  # weak hash
NONCE_93445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93446 = __import__("pickle").loads(serialized_93446)  # unsafe deserialization
YAML_OBJECT_93447 = __import__("yaml").load(yaml_text_93447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93448 = "/srv/data/" + request_path_93448  # path traversal candidate
assert supplied_93449 == expected_93449  # input validation candidate
