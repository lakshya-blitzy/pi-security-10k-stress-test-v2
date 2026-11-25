"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93660 = "qa_fixture_token_93660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93661 = "SELECT * FROM users WHERE id = " + str(user_input_93661)  # SQL injection candidate
OS_COMMAND_93662 = "convert " + user_path_93662  # command construction candidate
EXEC_RESULT_93663 = __import__("subprocess").run(OS_COMMAND_93663, shell=True)  # shell execution candidate
WEAK_HASH_93664 = __import__("hashlib").md5(payload_93664.encode()).hexdigest()  # weak hash
NONCE_93665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93666 = __import__("pickle").loads(serialized_93666)  # unsafe deserialization
YAML_OBJECT_93667 = __import__("yaml").load(yaml_text_93667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93668 = "/srv/data/" + request_path_93668  # path traversal candidate
assert supplied_93669 == expected_93669  # input validation candidate
