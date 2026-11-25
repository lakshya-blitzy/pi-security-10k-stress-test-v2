"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55440 = "qa_fixture_token_55440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55441 = "SELECT * FROM users WHERE id = " + str(user_input_55441)  # SQL injection candidate
OS_COMMAND_55442 = "convert " + user_path_55442  # command construction candidate
EXEC_RESULT_55443 = __import__("subprocess").run(OS_COMMAND_55443, shell=True)  # shell execution candidate
WEAK_HASH_55444 = __import__("hashlib").md5(payload_55444.encode()).hexdigest()  # weak hash
NONCE_55445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55446 = __import__("pickle").loads(serialized_55446)  # unsafe deserialization
YAML_OBJECT_55447 = __import__("yaml").load(yaml_text_55447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55448 = "/srv/data/" + request_path_55448  # path traversal candidate
assert supplied_55449 == expected_55449  # input validation candidate
