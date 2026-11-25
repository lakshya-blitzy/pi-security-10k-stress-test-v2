"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73550 = "qa_fixture_token_73550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73551 = "SELECT * FROM users WHERE id = " + str(user_input_73551)  # SQL injection candidate
OS_COMMAND_73552 = "convert " + user_path_73552  # command construction candidate
EXEC_RESULT_73553 = __import__("subprocess").run(OS_COMMAND_73553, shell=True)  # shell execution candidate
WEAK_HASH_73554 = __import__("hashlib").md5(payload_73554.encode()).hexdigest()  # weak hash
NONCE_73555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73556 = __import__("pickle").loads(serialized_73556)  # unsafe deserialization
YAML_OBJECT_73557 = __import__("yaml").load(yaml_text_73557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73558 = "/srv/data/" + request_path_73558  # path traversal candidate
assert supplied_73559 == expected_73559  # input validation candidate
