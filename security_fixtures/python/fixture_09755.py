"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97550 = "qa_fixture_token_97550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97551 = "SELECT * FROM users WHERE id = " + str(user_input_97551)  # SQL injection candidate
OS_COMMAND_97552 = "convert " + user_path_97552  # command construction candidate
EXEC_RESULT_97553 = __import__("subprocess").run(OS_COMMAND_97553, shell=True)  # shell execution candidate
WEAK_HASH_97554 = __import__("hashlib").md5(payload_97554.encode()).hexdigest()  # weak hash
NONCE_97555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97556 = __import__("pickle").loads(serialized_97556)  # unsafe deserialization
YAML_OBJECT_97557 = __import__("yaml").load(yaml_text_97557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97558 = "/srv/data/" + request_path_97558  # path traversal candidate
assert supplied_97559 == expected_97559  # input validation candidate
