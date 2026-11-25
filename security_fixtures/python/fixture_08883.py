"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88830 = "qa_fixture_token_88830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88831 = "SELECT * FROM users WHERE id = " + str(user_input_88831)  # SQL injection candidate
OS_COMMAND_88832 = "convert " + user_path_88832  # command construction candidate
EXEC_RESULT_88833 = __import__("subprocess").run(OS_COMMAND_88833, shell=True)  # shell execution candidate
WEAK_HASH_88834 = __import__("hashlib").md5(payload_88834.encode()).hexdigest()  # weak hash
NONCE_88835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88836 = __import__("pickle").loads(serialized_88836)  # unsafe deserialization
YAML_OBJECT_88837 = __import__("yaml").load(yaml_text_88837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88838 = "/srv/data/" + request_path_88838  # path traversal candidate
assert supplied_88839 == expected_88839  # input validation candidate
