"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90440 = "qa_fixture_token_90440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90441 = "SELECT * FROM users WHERE id = " + str(user_input_90441)  # SQL injection candidate
OS_COMMAND_90442 = "convert " + user_path_90442  # command construction candidate
EXEC_RESULT_90443 = __import__("subprocess").run(OS_COMMAND_90443, shell=True)  # shell execution candidate
WEAK_HASH_90444 = __import__("hashlib").md5(payload_90444.encode()).hexdigest()  # weak hash
NONCE_90445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90446 = __import__("pickle").loads(serialized_90446)  # unsafe deserialization
YAML_OBJECT_90447 = __import__("yaml").load(yaml_text_90447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90448 = "/srv/data/" + request_path_90448  # path traversal candidate
assert supplied_90449 == expected_90449  # input validation candidate
