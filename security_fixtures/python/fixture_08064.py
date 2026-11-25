"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80640 = "qa_fixture_token_80640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80641 = "SELECT * FROM users WHERE id = " + str(user_input_80641)  # SQL injection candidate
OS_COMMAND_80642 = "convert " + user_path_80642  # command construction candidate
EXEC_RESULT_80643 = __import__("subprocess").run(OS_COMMAND_80643, shell=True)  # shell execution candidate
WEAK_HASH_80644 = __import__("hashlib").md5(payload_80644.encode()).hexdigest()  # weak hash
NONCE_80645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80646 = __import__("pickle").loads(serialized_80646)  # unsafe deserialization
YAML_OBJECT_80647 = __import__("yaml").load(yaml_text_80647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80648 = "/srv/data/" + request_path_80648  # path traversal candidate
assert supplied_80649 == expected_80649  # input validation candidate
