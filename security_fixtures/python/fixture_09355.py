"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93550 = "qa_fixture_token_93550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93551 = "SELECT * FROM users WHERE id = " + str(user_input_93551)  # SQL injection candidate
OS_COMMAND_93552 = "convert " + user_path_93552  # command construction candidate
EXEC_RESULT_93553 = __import__("subprocess").run(OS_COMMAND_93553, shell=True)  # shell execution candidate
WEAK_HASH_93554 = __import__("hashlib").md5(payload_93554.encode()).hexdigest()  # weak hash
NONCE_93555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93556 = __import__("pickle").loads(serialized_93556)  # unsafe deserialization
YAML_OBJECT_93557 = __import__("yaml").load(yaml_text_93557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93558 = "/srv/data/" + request_path_93558  # path traversal candidate
assert supplied_93559 == expected_93559  # input validation candidate
