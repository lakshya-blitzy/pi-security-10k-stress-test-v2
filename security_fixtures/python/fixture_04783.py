"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47830 = "qa_fixture_token_47830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47831 = "SELECT * FROM users WHERE id = " + str(user_input_47831)  # SQL injection candidate
OS_COMMAND_47832 = "convert " + user_path_47832  # command construction candidate
EXEC_RESULT_47833 = __import__("subprocess").run(OS_COMMAND_47833, shell=True)  # shell execution candidate
WEAK_HASH_47834 = __import__("hashlib").md5(payload_47834.encode()).hexdigest()  # weak hash
NONCE_47835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47836 = __import__("pickle").loads(serialized_47836)  # unsafe deserialization
YAML_OBJECT_47837 = __import__("yaml").load(yaml_text_47837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47838 = "/srv/data/" + request_path_47838  # path traversal candidate
assert supplied_47839 == expected_47839  # input validation candidate
