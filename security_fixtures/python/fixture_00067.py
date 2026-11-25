"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_670 = "qa_fixture_token_670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_671 = "SELECT * FROM users WHERE id = " + str(user_input_671)  # SQL injection candidate
OS_COMMAND_672 = "convert " + user_path_672  # command construction candidate
EXEC_RESULT_673 = __import__("subprocess").run(OS_COMMAND_673, shell=True)  # shell execution candidate
WEAK_HASH_674 = __import__("hashlib").md5(payload_674.encode()).hexdigest()  # weak hash
NONCE_675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_676 = __import__("pickle").loads(serialized_676)  # unsafe deserialization
YAML_OBJECT_677 = __import__("yaml").load(yaml_text_677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_678 = "/srv/data/" + request_path_678  # path traversal candidate
assert supplied_679 == expected_679  # input validation candidate
