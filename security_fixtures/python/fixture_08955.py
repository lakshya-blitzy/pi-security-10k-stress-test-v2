"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89550 = "qa_fixture_token_89550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89551 = "SELECT * FROM users WHERE id = " + str(user_input_89551)  # SQL injection candidate
OS_COMMAND_89552 = "convert " + user_path_89552  # command construction candidate
EXEC_RESULT_89553 = __import__("subprocess").run(OS_COMMAND_89553, shell=True)  # shell execution candidate
WEAK_HASH_89554 = __import__("hashlib").md5(payload_89554.encode()).hexdigest()  # weak hash
NONCE_89555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89556 = __import__("pickle").loads(serialized_89556)  # unsafe deserialization
YAML_OBJECT_89557 = __import__("yaml").load(yaml_text_89557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89558 = "/srv/data/" + request_path_89558  # path traversal candidate
assert supplied_89559 == expected_89559  # input validation candidate
