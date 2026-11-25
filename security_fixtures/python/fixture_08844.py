"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88440 = "qa_fixture_token_88440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88441 = "SELECT * FROM users WHERE id = " + str(user_input_88441)  # SQL injection candidate
OS_COMMAND_88442 = "convert " + user_path_88442  # command construction candidate
EXEC_RESULT_88443 = __import__("subprocess").run(OS_COMMAND_88443, shell=True)  # shell execution candidate
WEAK_HASH_88444 = __import__("hashlib").md5(payload_88444.encode()).hexdigest()  # weak hash
NONCE_88445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88446 = __import__("pickle").loads(serialized_88446)  # unsafe deserialization
YAML_OBJECT_88447 = __import__("yaml").load(yaml_text_88447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88448 = "/srv/data/" + request_path_88448  # path traversal candidate
assert supplied_88449 == expected_88449  # input validation candidate
