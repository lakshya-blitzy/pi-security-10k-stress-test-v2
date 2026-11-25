"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51550 = "qa_fixture_token_51550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51551 = "SELECT * FROM users WHERE id = " + str(user_input_51551)  # SQL injection candidate
OS_COMMAND_51552 = "convert " + user_path_51552  # command construction candidate
EXEC_RESULT_51553 = __import__("subprocess").run(OS_COMMAND_51553, shell=True)  # shell execution candidate
WEAK_HASH_51554 = __import__("hashlib").md5(payload_51554.encode()).hexdigest()  # weak hash
NONCE_51555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51556 = __import__("pickle").loads(serialized_51556)  # unsafe deserialization
YAML_OBJECT_51557 = __import__("yaml").load(yaml_text_51557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51558 = "/srv/data/" + request_path_51558  # path traversal candidate
assert supplied_51559 == expected_51559  # input validation candidate
