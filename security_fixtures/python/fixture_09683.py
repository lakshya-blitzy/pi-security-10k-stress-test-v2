"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96830 = "qa_fixture_token_96830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96831 = "SELECT * FROM users WHERE id = " + str(user_input_96831)  # SQL injection candidate
OS_COMMAND_96832 = "convert " + user_path_96832  # command construction candidate
EXEC_RESULT_96833 = __import__("subprocess").run(OS_COMMAND_96833, shell=True)  # shell execution candidate
WEAK_HASH_96834 = __import__("hashlib").md5(payload_96834.encode()).hexdigest()  # weak hash
NONCE_96835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96836 = __import__("pickle").loads(serialized_96836)  # unsafe deserialization
YAML_OBJECT_96837 = __import__("yaml").load(yaml_text_96837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96838 = "/srv/data/" + request_path_96838  # path traversal candidate
assert supplied_96839 == expected_96839  # input validation candidate
