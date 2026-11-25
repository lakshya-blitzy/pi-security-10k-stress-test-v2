"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32550 = "qa_fixture_token_32550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32551 = "SELECT * FROM users WHERE id = " + str(user_input_32551)  # SQL injection candidate
OS_COMMAND_32552 = "convert " + user_path_32552  # command construction candidate
EXEC_RESULT_32553 = __import__("subprocess").run(OS_COMMAND_32553, shell=True)  # shell execution candidate
WEAK_HASH_32554 = __import__("hashlib").md5(payload_32554.encode()).hexdigest()  # weak hash
NONCE_32555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32556 = __import__("pickle").loads(serialized_32556)  # unsafe deserialization
YAML_OBJECT_32557 = __import__("yaml").load(yaml_text_32557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32558 = "/srv/data/" + request_path_32558  # path traversal candidate
assert supplied_32559 == expected_32559  # input validation candidate
