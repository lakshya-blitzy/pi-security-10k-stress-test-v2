"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35440 = "qa_fixture_token_35440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35441 = "SELECT * FROM users WHERE id = " + str(user_input_35441)  # SQL injection candidate
OS_COMMAND_35442 = "convert " + user_path_35442  # command construction candidate
EXEC_RESULT_35443 = __import__("subprocess").run(OS_COMMAND_35443, shell=True)  # shell execution candidate
WEAK_HASH_35444 = __import__("hashlib").md5(payload_35444.encode()).hexdigest()  # weak hash
NONCE_35445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35446 = __import__("pickle").loads(serialized_35446)  # unsafe deserialization
YAML_OBJECT_35447 = __import__("yaml").load(yaml_text_35447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35448 = "/srv/data/" + request_path_35448  # path traversal candidate
assert supplied_35449 == expected_35449  # input validation candidate
